using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PDFMaker.Parser
{
    public class Row
    {
        public Queue<Column> Columns { get; set; }
        public int Height { get; set; }
        public int Width { get; set; }
        public int PosX { get; set; }
        public int PosY { get; set; }

        public Row()
        {
            Columns = new Queue<Column>();
            Height = -1;
            Width = -1;
            PosX = -1;
            PosY = -1;
        
        }

        public void getColumnsPositions()
        {
            int prevWidth = 0;
            foreach (Column c in Columns)
            {
                c.PosX = PosX + prevWidth;
                prevWidth += c.Width;
                c.PosY = PosY;
                c.getElementsPositions();
            }
        }

        public void WriteToPdf(PdfDocument doc)
        {
            int spacing = 0;

            PDFMaker.RectArea b = new PDFMaker.RectArea(PosX, PosY, Width, Height, false);
            b.SetFillColor(0, 0, 0, 24);
            b.SetStrokeColor(0, 0, 0, 200);
            b.Filled = true;
            b.Stroked = false;
            b.AddToDocument(doc);
            doc.Flush();

            foreach (Column c in Columns)
                c.WriteToPdf(doc);
        }

        public void getColumnsWidthHeight()
        {
            int maxHeight = -1;
            bool calculatewidth = (Width == -1) ? true : false;

            if (calculatewidth)
                Width = 0;

            foreach (Column c in Columns)
            {
                c.getElementsWidthHeight();
                if (c.Height > maxHeight)
                    maxHeight = c.Height;

                if (calculatewidth)
                    Width += c.Width;

            }
            
            Height = maxHeight;
        }
    }
}
