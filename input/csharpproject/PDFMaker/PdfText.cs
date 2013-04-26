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
    public class PdfText
    {
        public string Text { get; set; }
        public int X { get; set; }
        public int Y { get; set; }
        public Font Font { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }
        public float Size { get{return Font.Size;} set{Font.Size=value;} }
        public int colorC { get; set; }
        public int colorM { get; set; }
        public int colorY { get; set; }
        public int colorK { get; set; }



        public PdfText(string text, int posX, int posY, Font font)
        {
            Text = text;
            X = posX;
            Y = posY;
            Font = font;
            colorC = 0;
            colorM = 0;
            colorY = 0;
            colorK = 225;
            Width = 1000;
            Height = 100;
        }

        public void AddToDocument(PdfDocument doc)
        {
            //doc.GetWriter.BeginText();
            //doc.GetWriter.SetFontAndSize(iTextSharp.text.pdf.BaseFont.CreateFont(), Size);
            doc.GetWriter.SetCMYKColorStroke(colorC, colorM, colorY, colorK);
            doc.GetWriter.SetCMYKColorFill(colorC, colorM, colorY, colorK);

            ColumnText ct = new ColumnText(doc.GetWriter);
            ct.SetSimpleColumn(X, Y, Width, Height);
            Phrase p = new Paragraph(Text, Font);
            ct.AddText(p);
            ct.Go();
            //doc.GetWriter.EndText();
            doc.Flush();
        }


    }
}
