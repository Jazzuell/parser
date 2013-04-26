using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PDFMaker.Parser.Elements
{
    class Field : Element
    {
        public Field() 
        {
          Text="";
          Name = "Field";
          Width=-1;
          Height = -1;
          PosX=-1;
          PosY=-1;
        }

        public override string ToString()
        {
            return "Field " + Text;
        }

        public override void getElementWidthHeight()
        {
            if (Width == -1)
                Width = 100;
            if (Height == -1)
                Height = 30;
        }


        public override void WriteToPdf(PdfDocument doc)
        {
            // to do 

            RectArea rect = new RectArea(PosX, PosY, Width, Height, false);
            rect.SetFillColor(0, 0, 0, 0);
            rect.SetStrokeColor(0, 0, 0, 250);
            rect.Stroked = true;
            rect.AddToDocument(doc);
        }
    }
}
