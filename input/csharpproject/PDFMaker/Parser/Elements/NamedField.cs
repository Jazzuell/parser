using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using iTextSharp.text.pdf;
using iTextSharp.text;
using iTextSharp;
namespace PDFMaker.Parser.Elements
{
    class NamedField : Element
    {
        public Label Label { get; set; }
        public string LabelPosition { get; set; }
        public int FieldFontSize { get; set; }
        public int FieldHeight { get; set; }
        public int FieldWidth { get; set; }
        public string Align { get; set; }
        BaseFont customfont; 

        public NamedField()
        {
          this.Label = new Label();
          Text="";
          Name = "NamedField";
          Width=-1;
          Height = -1;
          PosX=-1;
          PosY=-1;
          LabelPosition = "up";
          FieldFontSize = 9;
          FieldHeight = -1;
          FieldWidth = -1;
          Align = "left";
        }

        public override string ToString()
        {
            return "NamedField " + Text;
        }

        public override void getElementWidthHeight()
        {
            Label.getElementWidthHeight();
            if (Width == -1)
                if (Label.Width > (int)customfont.GetWidthPointKerned(Text, FieldFontSize))
                    Width = Label.Width +5;
                else
                    Width = (int)customfont.GetWidthPointKerned(Text, FieldFontSize)+5;

            if (Height == -1)
                if (Label.Text != "")
                    Height = FieldHeight + Label.Height;
                else
                    Height = FieldHeight;
        }

        public override void WriteToPdf(PdfDocument doc)
        {
            //  LABEL
            //  ---------------
            // | Hodnota(Text) |
            //  ---------------



            // biely stvorec obsahujuci hodnotu elementu  (ulozenu v Text)
            // sirka bieleho pola je priamoumerna dlzke textu ktory v nej bude vykresleny
            if (FieldWidth == -1)
                FieldWidth = 15 + (int)customfont.GetWidthPointKerned(Text, FieldFontSize);
            if (FieldHeight == -1)
                FieldHeight = FieldFontSize + 2;
            RectArea r = new RectArea(PosX + 1, PosY +2, FieldWidth+2, FieldHeight);
            r.SetFillColor(0, 0, 0, 0);
            r.AddToDocument(doc);


            if (Label.Text != "")
            {
                // vykreslenie labelu, ktory popisuje hodnoty nizsie
                Label.PosX = this.PosX + 3;
                Label.PosY = this.PosY + FieldHeight + 3;
                Label.WriteToPdf(doc);
            }

            // vpisanie hodnoty elementu do bieleho pola
            Label l = new Label();
            l.Width = FieldWidth-10;
            l.Height = FieldHeight;
            l.Text = this.Text;
            l.PosX = PosX ;
            l.PosY = PosY + 4;
            l.FontSize = FieldFontSize;
            if (FieldWidth > -1)
                l.Width = FieldWidth;
            if (FieldHeight >= -1)
                l.Height = FieldHeight;
            l.WriteToPdf(doc);

        }
    }
}
