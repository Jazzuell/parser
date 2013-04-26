using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PDFMaker.Parser
{
    class RowSpace : Row
    {
        public RowSpace(int heigh)
        {
            Row r = new Row();
            //r.Width = (int)iTextSharp.text.PageSize.A4.Width-150;
            Column s = new Column();
            s.Height = heigh;
            //s.Width = (int)iTextSharp.text.PageSize.A4.Width - 50;
            Columns.Enqueue(s);
        }
    }
}
