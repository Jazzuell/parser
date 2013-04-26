using System;
using PDFMaker;
using iTextSharp;
using iTextSharp.text;


namespace PDFMaker
{
    public class PdfImage
    {
        private Image L;

        public int X { get; set; }
        public int Y { get; set; }
        private string _path;

        public int Height { get; set; }
        public int Width { get; set; }


        public PdfImage(string path, int x, int y, int h, int w)

        { }
        public PdfImage(string path, int x, int y)
            : this(path, x, y, -1, -1)
        {
            _path = path;
            L = Image.GetInstance(_path);
            X = x;
            Y = y;
        }

        public PdfImage(string path)
            : this(path, 0, 0)
        { }

        public void AddLogo(PdfDocument doc, int x, int y) 
        {
            L= Image.GetInstance(_path);
            L.SetAbsolutePosition(x,y);
            doc.AddElement(L);
            doc.Flush();
        }

        public void AddAsTopLogo(PdfDocument doc) 
        {
            throw new NotImplementedException();
        }

        public void AddAsTopLeftLogo(PdfDocument doc)
        {
            throw new NotImplementedException();
        }

        public void AddAsTopRightLogo(PdfDocument doc)
        {
            AddLogo(doc, (int)doc.PageSize.Width - (int)L.Width, (int)doc.PageSize.Height - (int)L.Height);
        }

        public void AddAsBottomLeftLogo(PdfDocument doc)
        {
            throw new NotImplementedException();
        }

        public void AddAsBottomLogo(PdfDocument doc)
        {
            throw new NotImplementedException();
        }

        public void AddAsTopBottomRightLogo(PdfDocument doc)
        {
            throw new NotImplementedException();
        }
    }
}
