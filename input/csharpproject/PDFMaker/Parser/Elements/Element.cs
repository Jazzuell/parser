using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PDFMaker.Parser.Elements
{
    public class Element
    {
        public int PosX { get; set; }
        public int PosY { get; set; }
        public int Width  { get; set; }
        public int Height { get; set; }

        public string Text { get; set; }
        public string Name { get; set; }

        public virtual void getElementWidthHeight()
        {
        }

        public virtual void WriteToPdf(PdfDocument doc)
        {
        }
    }
}
