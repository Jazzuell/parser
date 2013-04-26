using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp;
using iTextSharp.text;
using System.IO;
using iTextSharp.text.pdf;
namespace PDFMaker
{
    public class RectArea
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
        private int _fillM;
        private int _fillY;
        private int _fillK;

        public float Radius { get; set; }  
        public bool Filled { get; set; }  
        public bool Stroked { get; set; } 
        public int StrokeSize { get; set; }



        public RectArea(float posx, float posy, float width, float heigh, bool rounded)
        {
            _posx = posx;
            _posy = posy;
            _width = width;
            _heigh = heigh;
            if (rounded)
                Radius = 20.0F;
            else
                Radius = 0.0F;

            _strokeC=0;
            _strokeM=0;
            _strokeY=0;
            _strokeK = 80;


            _fillC = 50;
            _fillM = 20;
            _fillY = 0;
            _fillK = 5;

            StrokeSize = 0;

            Filled = true;
            Stroked = true;

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
            if (_posx < doc.Margins[0]) { _posx=doc.Margins[0];};
            if (_posx > doc.PageSize.Width - doc.Margins[1]) { _posx = doc.PageSize.Width - doc.Margins[1]; };
            if (_posy < doc.Margins[3]){_posy=doc.Margins[3];};
            if (_posy > doc.PageSize.Height - doc.Margins[2]) {_posy =doc.PageSize.Height - doc.Margins[2]; };

            if (_heigh < 1) _heigh = 1;
            if (_heigh > doc.PageSize.Height - doc.Margins[2] - doc.Margins[3]-_heigh) _heigh = doc.PageSize.Height - doc.Margins[2] - doc.Margins[3];
            if (_width < 1) _width = 1;
            if (_width+_posx > doc.PageSize.Width - doc.Margins[1]) _width = doc.PageSize.Width  - doc.Margins[1]-_posx;

            doc.GetWriter.SetCMYKColorStroke(_strokeC, _strokeM, _strokeY, _strokeK);
            doc.GetWriter.SetCMYKColorFill(_fillC, _fillM, _fillY, _fillK);
            doc.GetWriter.SetLineWidth(StrokeSize);

            //doc.GetWriter.RoundRectangle(
            doc.GetWriter.RoundRectangle(_posx, _posy, _width, _heigh, Radius);

            if (Stroked)
                if (Filled)
                    doc.GetWriter.FillStroke();
                else
                    doc.GetWriter.Stroke();
            else
                doc.GetWriter.Fill();
            
            doc.Flush();
        }
    }
}
