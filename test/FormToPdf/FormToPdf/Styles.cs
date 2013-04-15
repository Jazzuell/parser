using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using iTextSharp;
using iTextSharp.text;
namespace FormToPdf
{
    public static class Styles
    {
        private static float DEFAULT_FONT_SIZE = 12f;
        private static string DEFAULT_FONT = "Arial";
        private static BaseColor DEFAULT_FONT_COLOR = BaseColor.BLACK;
        private static int DEFAULT_FONT_STYLE = 10;

        public static Font FontHeader1 { get; set; }
        public static Font FontHeader2 { get; set; }
        public static Font FontHeader3 { get; set; }
        public static Font FontNormal { get; set; }
        public static Font FontItalic { get; set; }
        public static Font FontBold { get; set; }
        public static Font FontUnerline { get; set; }
        public static List<NamedFont> CustomFonts { get; set; }


        static Styles()
        {
            CustomFonts  = new List<NamedFont>();
            FontHeader1  = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE + 8, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            FontHeader2  = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE + 4, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            FontHeader3  = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE + 2, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            FontNormal   = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            FontItalic   = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            FontBold     = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            FontUnerline = FontFactory.GetFont(DEFAULT_FONT, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, DEFAULT_FONT_COLOR);
            
        }

        public static bool IsFontRegistered(string NameOfFont)
        {
            foreach (NamedFont font in CustomFonts)
            {
                if (font.ToString() == NameOfFont)
                    return true;
            }
            return false;
        }

        public static void RegisterFont(NamedFont font)
        {
            if (font != null)
            {
                if (IsFontRegistered(font.ToString()))
                    throw new DuplicateNameException();
                CustomFonts.Add(font);
            }
            else
                throw new NullReferenceException();
        }

    }
}
