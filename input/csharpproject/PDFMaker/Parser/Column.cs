using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using PDFMaker.Parser.Elements;


namespace PDFMaker.Parser
{
    public class Column
    {
        public string Align { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }
        public int PosX { get; set; }
        public int PosY { get; set; }
        public Queue<Element> Elements { get; set; }


        public Column()
        {
            Align = "center";
            Width = XmlParser.CalculateWidth("A4");
            Elements = new Queue<Element>();
            Height = -1;
            Width = -1;
        }

        public void WriteToPdf(PdfDocument doc)
        { 
            foreach (Element e in Elements)
                e.WriteToPdf(doc);

            if (doc.DEBUG)
            {
                RectArea r = new RectArea(PosX, PosY, Width, Height);
                r.Filled = false;
                r.Stroked = true;
                r.SetStrokeColor(0, 0, 0, 250);
                r.AddToDocument(doc);
            }

        }

        public void getElementsPositions()
        {
            int prevHeight = 0;
            int pomY = PosY;
            foreach (Element e in Elements)
            {
                e.getElementWidthHeight();
                e.PosX = PosX;
                e.PosY = pomY - prevHeight;
                pomY = pomY - prevHeight;
                prevHeight += e.Height;
                //e.getElementsPositions();
            }
        }

        public void getElementsWidthHeight()
        {
            foreach (Elements.Element e in Elements)
            {
                // taketo odbocky a vynimky nie su vhodne z hladiska univerzalnosti
                // treba to riesit inak
                //if (e is Label)
                //{
                //    e.Width = Width;
                //}
                e.getElementWidthHeight();
                if (e.Width > Width)
                    e.Width = Width;
            }

            if (Width==-1)
                foreach (Elements.Element e in Elements)
                {
                    if (e.Width>Width)
                        Width = e.Width;
                
                }

            if (Height == -1)
                foreach (Elements.Element e in Elements)
                {
                    Height += e.Height;
                }
        }
    }
}
