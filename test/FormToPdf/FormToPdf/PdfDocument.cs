using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using iTextSharp.text;
using iTextSharp.text.pdf;

namespace FormToPdf
{
    public class PdfDocument
    {
        private static Rectangle DEFAULT_PAGESIZE = iTextSharp.text.PageSize.A4;
        private Document _Document;
        private Rectangle _PageSize;
        private string _docPath;
        private List<float> _margins;
        public static readonly PageSize PageFormats;

        public string DocumentPath { get { return _docPath; }}  // path of the final pdf document
        public Rectangle PageSize { get { return _PageSize; } }    // actual size of page, chosed from iTextSharp.text.Pagesize.
        public List<float> Margins { get { return _margins; } } // margins of elements in document in order left,right,top,bottom
        public Rectangle DefaultPageSize { get { return DEFAULT_PAGESIZE; } } // default size of page

        public PdfDocument(string documentPath)
            : this(documentPath, DEFAULT_PAGESIZE, 25, 25, 50, 25)
        {
        }

        public PdfDocument(string documentPath, Rectangle pageSize)
            : this(documentPath, pageSize, 25, 25, 50, 25)
        {
        }

        public PdfDocument(string documentPath,
            float LeftMargin, float RightMargin, float TopMargin, float BottomMargin)
            : this(documentPath, DEFAULT_PAGESIZE, LeftMargin, RightMargin, TopMargin, BottomMargin)
        {
        }

        public PdfDocument(string documentPath, Rectangle pageSize,
            float LeftMargin, float RightMargin, float TopMargin, float BottomMargin)
        {
            _docPath = documentPath;
            _PageSize = pageSize;
            _margins = new List<float>(4);
            _margins.Add(LeftMargin);   //margin left
            _margins.Add(RightMargin);  //margin right
            _margins.Add(TopMargin);    //margin top
            _margins.Add(BottomMargin); //margin bottom

            InitializeDocument();
        }

        private void InitializeDocument()
        {
            _Document = new Document(_PageSize, Margins[0], Margins[1], Margins[2], Margins[3]);
            try
            {
                PdfWriter.GetInstance(_Document, new FileStream(DocumentPath, FileMode.Create));
            }
            catch (Exception exception)
            {
                throw exception;
            }
            finally
            {
                _Document.Open();
            }
        }

        ~PdfDocument()
        {
            this.Save();
        }

        public void Save()
        {
            _Document.Close();
        }

        public void AddElement(IElement element)
        {
            _Document.Add(element);
        }

    }
}
