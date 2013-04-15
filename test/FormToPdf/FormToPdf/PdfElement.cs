using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp;
using iTextSharp.text;
namespace FormToPdf
{
    interface PdfElement
    {
        void AddToDocument(Document document);
    }
}
