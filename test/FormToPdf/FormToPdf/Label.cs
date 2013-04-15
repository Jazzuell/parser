using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp.text;

namespace FormToPdf
{
    class Label : PdfElement
    {
        private string _text;
        private Font _font;
        private iTextSharp.text.Paragraph _paragraph;
        public Font Font 
        { 
            get
            {
                return _font;
            } 
            set 
            { 
                _font = value; 
                _paragraph = new Paragraph(_text,_font);
             }
        }

        public string Text
        {
            get
            {
                return _text;
            }
            set 
            { 
                _text = value;
                _paragraph = new Paragraph(_text,_font);
            }
        }

        Label(string text):this(text,Styles.FontNormal)
        {
        }

        Label(Font font):this("",font)
        {
        }

        Label():this("")
        {
        }

        Label(string text, Font font)
        {
            _text = text;
            Font = font;
            _paragraph = new Paragraph(_text,font);
        }

        public void AddToDocument(Document document)
        {
            //_paragraph.se
            document.Add(_paragraph);
            
           
        }
    }
}
