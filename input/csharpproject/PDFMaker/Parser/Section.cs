using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp;
using iTextSharp.text;
using PDFMaker;
using System.IO;
using iTextSharp.text.pdf;
using PDFMaker.Parser.Elements;
namespace PDFMaker.Parser
{
    public class Section
    {
        private BaseFont customfont; 
        
        public int PosX { get; set; }
        public int PosY { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }
        
        public List<int> Margins;

        public Queue<Row> Rows;

        public int FontSize { get; set; }
        public string Label { get; set; }

        public bool Rounded { get; set; }
        public float Radius { get; set; }

        public bool Filled { get; set; }  
        public bool Stroked { get; set; } 
        public double StrokeSize { get; set; }

        public string TextHeader { get; set; }
        public string TextBody { get; set; }


        private int _strokeC = 255;
        private int _strokeM = 0;
        private int _strokeY = 0;
        private int _strokeK = 0;
        private int _fillC = 172;
        private int _fillM = 104;
        private int _fillY = 20;
        private int _fillK = 105;
        private int _labelC = 0;
        private int _labelM = 0;
        private int  _labelY = 0;
        private int _labelK = 0;

        public void SetStrokeColor(int C, int M, int Y, int K)
        {
            _strokeC = C;
            _strokeM = M;
            _strokeY = Y;
            _strokeK = K;
        }

        public void SetFillColor(int C, int M, int Y, int K)
        {
            _fillC = C;
            _fillM = M;
            _fillY = Y;
            _fillK = K;
        }

        public void SetLabelColor(int C, int M, int Y, int K)
        {
            _labelC = C;
            _labelM = M;
            _labelY = Y;
            _labelK = K;
        }


        public Section()
        {
            PosX = -1;
            PosY = -1;
            Width = -1;
            Height = -1;
            Rows = new Queue<Row>();

            RowSpace rs = new RowSpace(0);
            Rows.Enqueue(rs);


            Margins = new List<int>();

            Label = "";
            FontSize = 10;

            //Rounded = false;
            //Radius = (Rounded) ? 20.0F : 0.0F;
            Radius = 0.0F;

            StrokeSize = 1;

            Filled = true;
            Stroked = true;

            TextBody = "";
            TextHeader = "";
        }

        public void WriteToPdf(PdfDocument doc)
        {
            // kalibracia pozicie z pohladu odsadenia
            if (PosX < doc.Margins[0]) { PosX = (int)(doc.Margins[0]); };
            if (PosX > doc.PageSize.Width - doc.Margins[1]) { PosX = (int)(doc.PageSize.Width - doc.Margins[1]); };
            if (PosY < doc.Margins[3]) { PosY = (int)(doc.Margins[3]); };
            if (PosY > doc.PageSize.Height - doc.Margins[2]) { PosY = (int)(doc.PageSize.Height - doc.Margins[2]); };

            if (Height < 1) Height = 1;
            //if (Height > doc.PageSize.Height - doc.Margins[2] - doc.Margins[3]) Height = (int)(doc.PageSize.Height - doc.Margins[2] - doc.Margins[3]);
            if (Width < 1) Width = 1;
            //if (Width > doc.PageSize.Width - doc.Margins[0] - doc.Margins[1]) Width = (int)(doc.PageSize.Width - doc.Margins[0] - doc.Margins[1]);

            doc.GetWriter.SetLineWidth(1);


            /////////////////////////////////////////////////////////
             //vykreslenie spodneho obdlznika sluziaceho ako podklad
            PDFMaker.RectArea b = new PDFMaker.RectArea(PosX, PosY + Height-18, Width, 18, false);
            b.SetFillColor(_fillC, _fillM, _fillY, _fillK);
            b.SetStrokeColor(_strokeC, _strokeM, _strokeY, _strokeK);
            b.Filled = true;
            b.AddToDocument(doc);
            doc.Flush();
            //////////////////////////////////////////////////////


            // text hlavicky
            if (FontSize > 17)
                FontSize = 17;
            doc.GetWriter.SetCMYKColorStroke(_labelC, _labelM, _labelY, _labelK);
            doc.GetWriter.SetCMYKColorFill(_labelC, _labelM, _labelY, _labelK);
            doc.GetWriter.SetFontAndSize(customfont, FontSize);
            doc.GetWriter.BeginText();
            doc.GetWriter.SetTextMatrix(PosX + 10, PosY + Height - 14);
            
            doc.GetWriter.ShowText(Label);
            doc.GetWriter.EndText();
            doc.Flush();


            //text tela 
            doc.GetWriter.BeginText();
            doc.GetWriter.SetFontAndSize(customfont, FontSize);
            doc.GetWriter.SetCMYKColorStroke(0, 0, 0, 0);
            doc.GetWriter.SetCMYKColorFill(0, 0, 0, 255);
            
            ColumnText ct = new ColumnText(doc.GetWriter);
            ct.SetSimpleColumn(PosX + 25, PosY + Height - 28, Width-30, Height-30);
            Font font = new Font(customfont, FontSize);
            Phrase p = new Phrase(TextBody, font);
            ct.AddText(p);
            ct.Go();
            doc.GetWriter.EndText();
            doc.Flush();

            while (Rows.Count > 0) 
            {
                if (Rows.Peek().PosY < (int)doc.Margins[2])
                {
                    doc.AddNewPage();
                    doc.ActualWritePosition = (int)doc.PageSize.Top - (int)doc.Margins[2];
                    Height = -1;
                    getSectionWidthHeight();
                    this.PosY = doc.ActualWritePosition - Height;
                    this.getRowsPositions();
                    doc.Recalibrate();
                }
                
                Rows.Dequeue().WriteToPdf(doc);
            }
        }


        public void getRowsPositions()
        {
            int prevHeight = 0;
            foreach (Row r in Rows)
            {
                r.PosX = PosX;
                r.PosY = PosY + Height -18 - r.Height - prevHeight;
                prevHeight += r.Height;
                r.getColumnsPositions();
            }
        }

        public void getSectionWidthHeight()
        {
            bool calculatewidth = (Width == -1) ? true : false;
            bool calculateheight = (Height == -1) ? true : false;

            foreach (Row r in Rows)
            {
                r.getColumnsWidthHeight();
                if (calculateheight)
                {
                    Height += r.Height;
                }
                if (calculatewidth)
                {
                    if (r.Width > Width)
                        Width = r.Width;
                }
            }

            foreach (Row r in Rows)
            {
                r.Width = Width;
                //if (r.Width==-1 && r.Columns.Count==1)
                //    r.Columns.ElementAt(0).Width = Width;
            }
            if (calculateheight)
                Height += 22;
        }
    }
}
