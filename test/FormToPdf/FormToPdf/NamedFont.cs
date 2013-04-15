using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Org.BouncyCastle.Security;
using iTextSharp.text;

namespace FormToPdf
{
    public class NamedFont
    {
        private string _name;
        public Font Font { get; set; }
        public string Name{get{return _name; }}

        NamedFont(string name, Font font)
        {
            if (name =="" || font == null)
                throw new InvalidParameterException();
            Font = font;
            _name = name;
        }

        NamedFont(string name):this(name,Styles.FontNormal)
        {}

        public override string ToString()
        {
            return Name;
        }
    }
}
