using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp;
using iTextSharp.text;
using PDFMaker;
using System.IO;
using iTextSharp.text.pdf;
namespace PDFMaker
{
    public  class FormField
    {
        private float _posx;
        private float _posy;
        private float _width;
        private float _heigh;
        private int _strokeC;
        private int _strokeM;
        private int _strokeY;
        private int _strokeK;
        private int _fillC;
        private int  _fillM;
        private int  _fillY;
        private int _fillK;

        public float Radius { get; set; }
        public bool Filled { get; set; }  
        public bool Stroked { get; set; }
        public int StrokeSize { get; set; }

        public string TextHeader { get; set; }
        public string TextBody { get; set; }


        public FormField(float posx, float posy, float width, float heigh, bool rounded)
        {
            _posx = posx;
            _posy = posy;
            _width = width;
            _heigh = heigh;
            if (rounded)
                Radius = 20.0F;
            else
                Radius = 0.0F;

            _strokeC = 0;
            _strokeM = 0;
            _strokeY = 0;
            _strokeK = 250;
            
            _fillC = 172;
            _fillM = 104;
            _fillY = 20;
            _fillK = 105;
            StrokeSize = 2;

            Filled = true;
            Stroked = true;

            TextBody = "";
            TextHeader = "";

        }

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
        
        public void AddToDocument(PdfDocument doc)
        {
            // kalibracia pozicie z pohladu odsadenia
            if (_posx < doc.Margins[0]) { _posx = doc.Margins[0]; };
            if (_posx > doc.PageSize.Width - doc.Margins[1]) { _posx = doc.PageSize.Width - doc.Margins[1]; };
            if (_posy < doc.Margins[3]) { _posy = doc.Margins[3]; };
            if (_posy > doc.PageSize.Height - doc.Margins[2]) { _posy = doc.PageSize.Height - doc.Margins[2]; };

            if (_heigh < 1) _heigh = 1;
            if (_heigh > doc.PageSize.Height - doc.Margins[2] - doc.Margins[3]) _heigh = doc.PageSize.Height - doc.Margins[2] - doc.Margins[3];
            if (_width < 1) _width = 1;
            if (_width > doc.PageSize.Width - doc.Margins[0] - doc.Margins[1]) _width = doc.PageSize.Width - doc.Margins[0] - doc.Margins[1];

            // vykreslenie spodneho obdlznika sluziaceho ako podklad
            doc.GetWriter.SetLineWidth(StrokeSize);
            PDFMaker.RectArea b = new PDFMaker.RectArea(_posx,_posy, _width, _heigh, false);
            
            b.SetFillColor(_fillC, _fillM, _fillY, _fillK);
            b.SetStrokeColor(_strokeC, _strokeM, _strokeY, _strokeK);
            b.SetStrokeColor(_strokeC, _strokeM, _strokeY, _strokeK);
            b.Filled = true;
            b.AddToDocument(doc);
            if (Stroked)
                if (Filled)
                    doc.GetWriter.FillStroke();
                else
                    doc.GetWriter.Stroke();
            else
                doc.GetWriter.Fill();
            doc.Flush();

            // vykreslenie obdlznika sluziaceho ako horna vrstvva podkladu
            //doc.GetWriter.SetCMYKColorStroke(_strokeC, _strokeM, _strokeY, _strokeK);
            //doc.GetWriter.SetCMYKColorFill(_fillC, _fillM, _fillY, _fillK);
            PDFMaker.RectArea c = new PDFMaker.RectArea(_posx, _posy, _width, _heigh - 21, false);
            c.SetFillColor(0, 0, 0, 30);
            c.Filled = true;
            c.AddToDocument(doc);
            if (Stroked)
                if (Filled)
                    doc.GetWriter.FillStroke();
                else
                    doc.GetWriter.Stroke();
            else
                doc.GetWriter.Fill();
            doc.Flush();

            // text hlavicky
            doc.GetWriter.SetCMYKColorStroke(0, 0, 0, 0);
            doc.GetWriter.SetCMYKColorFill(0, 0, 0, 0);
            doc.GetWriter.BeginText();
            doc.GetWriter.SetTextMatrix(_posx + 25, _posy + _heigh - 18);
            BaseFont customfont = BaseFont.CreateFont();
            Font font = new Font(customfont, 12);
            doc.GetWriter.SetFontAndSize(customfont, 20.0F);
            doc.GetWriter.ShowText(TextHeader);
            doc.GetWriter.EndText();
            doc.Flush();

            //text tela 
            doc.GetWriter.BeginText();
            font = new Font(customfont, 12);
            doc.GetWriter.SetFontAndSize(customfont, 12.0F);
            doc.GetWriter.SetCMYKColorStroke(0, 0, 0, 255);
            doc.GetWriter.SetCMYKColorFill(0, 0, 0, 255);
            
            ColumnText ct = new ColumnText(doc.GetWriter);
            ct.SetSimpleColumn(_posx + 25, _posy + _heigh - 28, _width-30, _heigh-30);
            Phrase p = new Phrase(TextBody, font);
            ct.AddText(p);
            ct.Go();
            doc.GetWriter.EndText();
            doc.Flush();
        }
    }
}
