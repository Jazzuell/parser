using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp;
using iTextSharp.text;
using System.IO;
using iTextSharp.text.pdf;
using PDFMaker.Parser;

namespace PDFMaker
{
    public class PdfDocument
    {
        public bool DEBUG = false;



        public int ActualWritePosition = 0;


        private static Rectangle DEFAULT_PAGESIZE = iTextSharp.text.PageSize.A4;
        private Document _Document;
        private Rectangle _PageSize;
        private string _docPath;
        private List<float> _margins;
        public static PageSize PageFormats;
        private PdfContentByte _contentbyte;
        private PdfWriter _pdfWriter;


        public Queue<Parser.Section> Sections { get; set; }
        public string DocumentPath { get { return _docPath; } }
        public Rectangle PageSize { get { return _PageSize; } } 
        public List<float> Margins { get { return _margins; } } 
        public Rectangle DefaultPageSize { get { return DEFAULT_PAGESIZE; } } 
        public PdfContentByte GetWriter { get { return _contentbyte; } }



        public PdfDocument(string documentPath, Rectangle pageSize, float LeftMargin, float RightMargin, float TopMargin, float BottomMargin)
        {
            Sections = new Queue<Parser.Section>();

            _docPath = documentPath;
            _PageSize = pageSize;
            _margins = new List<float>(4);
            _margins.Add(LeftMargin); //margin left
            _margins.Add(RightMargin); //margin right
            _margins.Add(TopMargin); //margin top
            _margins.Add(BottomMargin); //margin bottom
            ActualWritePosition = (int)PageSize.Top - (int)_margins[2];


            InitializeDocument();
        }

        public PdfDocument(string documentPath)
            : this(documentPath, DEFAULT_PAGESIZE, 25, 25, 25, 25)
        {
        }

        public PdfDocument(string documentPath, Rectangle pageSize)
            : this(documentPath, pageSize, 25, 25, 25, 25)
        {
        }

        public PdfDocument(string documentPath, float LeftMargin, float RightMargin, float TopMargin, float BottomMargin)
            : this(documentPath, DEFAULT_PAGESIZE, LeftMargin, RightMargin, TopMargin, BottomMargin)
        {
        }


        private void InitializeDocument()
        {
            _Document = new Document(_PageSize, Margins[0], Margins[1], Margins[2], Margins[3]);
            try
            {
                _pdfWriter = PdfWriter.GetInstance(_Document, new FileStream(DocumentPath, FileMode.Create));
                _Document.Open();
                _contentbyte = _pdfWriter.DirectContent;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        public void AddElement(IElement element)
        {
            _Document.Add(element);
        }
        



        private void getSectionsPosition()
        {
            ActualWritePosition = (int)PageSize.Top - (int)_margins[2];

            while (Sections.Count > 0)
            {
                Recalibrate();
                Parser.Section pomS = Sections.Peek();
                int pomh = pomS.Height;                
                pomS.WriteToPdf(this);
                ActualWritePosition -= 20;
                ActualWritePosition -= pomh;
                Sections.Dequeue();
            }

        }




        public void Recalibrate()
        {

            foreach (PDFMaker.Parser.Section s in Sections)
            {
                s.Height = -1;
                s.getSectionWidthHeight();

                if (s.Width == -1)
                    s.Width = Convert.ToInt32(iTextSharp.text.PageSize.A4.Width) - 50;


                s.PosX = (int)_margins[0];
                s.PosY = ActualWritePosition - s.Height;
                s.getRowsPositions();
            }       
        }

        public void AddNewPage()
        {
            _Document.NewPage();
        }
        public void Save()
        {
            getSectionsPosition();
            try
            {
                _pdfWriter.Flush();
                _Document.Close();
            }
            catch (Exception e)
            {
                throw e;
            }
        }

        public void Flush()
        {
            try
            {
                _pdfWriter.Flush();
            }
            catch (Exception e)
            {
                throw e;
            }
        }
    }
}
