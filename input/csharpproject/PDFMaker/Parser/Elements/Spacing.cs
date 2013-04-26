using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PDFMaker.Parser.Elements
{
    class Spacing : Element
    {

        public Spacing()
        {
            Text = "";
            Name = "Spacing";
            Width = -1;
            Height = -1;
            PosX = -1;
            PosY = -1;
        }

        public override void getElementWidthHeight()
        {
            if (Width == -1)
                Width = 35;

            if (Height == -1)
                Height = 18;
        }


        public override string ToString()
        {
            return "Spacing " + Name;
        }

        public override void WriteToPdf(PdfDocument doc)
        {
           // to do 
        }
    }
}
