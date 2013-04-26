using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PDFMaker.Parser
{
    class PageBreak : Row
    {
        public void WriteToPdf(PdfDocument doc)
        {
            doc.AddNewPage();
        }
    }
}
