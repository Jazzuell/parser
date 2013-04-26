using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp.text.pdf;

namespace PDFMaker.Parser.Elements
{
    class Label : Element
    {
        public int FontSize { get; set; }
        public string Align { get; set; }
        private BaseFont customfont;
        public Label()
        {
           
            Name = "Label";
            Align = "left";
            FontSize = 11;
            Text = "";
            Width=-1;
            Height = -1;
            PosX=-1;
            PosY=-1;
        }


        public override string ToString()
        {
            return "Label " + Text;
        }

        public override void getElementWidthHeight()
        {
            if (Width==-1)
                Width = (int)customfont.GetWidthPointKerned(Text, FontSize);

            if (Height == -1)
                Height = FontSize;
        }

        public override void WriteToPdf(PdfDocument doc)
        {
            doc.GetWriter.SetCMYKColorStroke(0, 0, 0, 255);
            doc.GetWriter.SetCMYKColorFill(0, 0, 0, 255);
            doc.GetWriter.BeginText();
            doc.GetWriter.SetTextMatrix(PosX+2, PosY+2);
            
            while ((customfont.GetWidthPointKerned(Text, FontSize) > Width) || (FontSize == 2)) FontSize--;
            doc.GetWriter.SetFontAndSize(customfont, FontSize);
            doc.GetWriter.ShowText(Text);
            doc.GetWriter.EndText();
            doc.Flush();
        }

    }
}
