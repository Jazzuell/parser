using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using PDFMaker.Parser.Elements;
using PDFMaker.Parser;

namespace PDFMaker
{
    public static class XmlParser
    {
        static  PdfDocument document;

        public static int CalculateWidth(string s)
        {
            int width = -1;
            if (s.Contains("%"))
            {
                int.TryParse(s.Replace("%", ""), out width);
                width = (int)(((document.PageSize.Width - document.Margins[0] - document.Margins[1] )/ 100) * width);
            }
            else if (s.Contains("A4"))
            {
                int.TryParse(s.Replace("A4",""),out width);
                width = width + Convert.ToInt32(iTextSharp.text.PageSize.A4.Width) - (int)document.Margins[0] - (int)document.Margins[1];
            }
            else
                int.TryParse(s, out width);

            return width;
        }

        public static int CalculateHeight(string s)
        {
            int height = -1;
            if (s.Contains("%"))
            {
                int.TryParse(s.Replace("%", ""), out height);
                height = (int)(((document.PageSize.Height-document.Margins[2] - document.Margins[3]) / 100) * height);
            }
            else if (s.Contains("A4"))
            {
                int.TryParse(s.Replace("A4", ""), out height);
                height = height + Convert.ToInt32(iTextSharp.text.PageSize.A4.Height) - (int)document.Margins[2] - (int)document.Margins[3];
            }
            else
                int.TryParse(s, out height);

            return height;
        }

        public static void Parse(string path, string outputpath)
        {            
           XmlTextReader reader = new XmlTextReader(path);

           document = new PdfDocument(outputpath);

           string TextValue = "";
           Section section = new Section();
           Row row = new Row();
           Column column = new Column();
           Element element = new Element();

           while (reader.Read())
           {
               switch (reader.NodeType)
               {
                   case XmlNodeType.Element:
                       switch (reader.Name.ToLower())
                       {
               
                           case "section":
                               section = new Section();
                               while (reader.MoveToNextAttribute()) // Read the attributes.
                               {
                                   switch (reader.Name.ToLower())
                                   {
                                       case "label":
                                           section.Label = reader.Value;
                                           break;
                                       case "width":
                                           section.Width = CalculateWidth(reader.Value);
                                           break;
                                       case "height":
                                           section.Height = CalculateHeight(reader.Value);
                                           break;
                                       case "fontsize":
                                           section.FontSize = Convert.ToInt32(reader.Value);
                                           break;
                                       case "bgcolorcmyk":
                                           List<int> tmp = new List<int>();
                                           foreach (string color in reader.Value.Split(','))
                                           {
                                               tmp.Add(Convert.ToInt32(color));
                                           }
                                           section.SetFillColor(tmp[0], tmp[1], tmp[2], tmp[3]);
                                           break;
                                       case "strokecolorcmyk":
                                           List<int> tmp2 = new List<int>();
                                           foreach (string color in reader.Value.Split(','))
                                           {
                                               tmp2.Add(Convert.ToInt32(color));
                                           }
                                           section.SetStrokeColor(tmp2[0], tmp2[1], tmp2[2], tmp2[3]);
                                           break;
                                       case "marginssection":
                                           section.Margins = new List<int>();
                                           foreach (string color in reader.Value.Split(','))
                                           {
                                               section.Margins.Add(Convert.ToInt32(color));
                                           }
                                           break;
                                       case "textcolorcmyk":
                                           List<int> tmp3 = new List<int>();
                                           foreach (string color in reader.Value.Split(','))
                                           {
                                               tmp3.Add(Convert.ToInt32(color));
                                           }
                                           section.SetLabelColor(tmp3[0], tmp3[1], tmp3[2], tmp3[3]);
                                           break;
                                   }
                               }
                               break;

                           case "row":
                               row = new Row();
                               break;
            
                           case "column":
                               column = new Column();
                               while (reader.MoveToNextAttribute())
                                   switch (reader.Name.ToLower())
                                   {
                                       case "width":
                                           column.Width=CalculateWidth(reader.Value);
                                           break;
                                       case "height":
                                           column.Height = CalculateHeight(reader.Value);
                                           break;
                                       case "align":
                                           column.Align=reader.Value;
                                           break;
                                       default:
                                           throw new Exception();
                                   }                                    
                               break;

                           case "element":
                               reader.MoveToNextAttribute();
                               if (reader.Name.ToLower() !="type")
                                   throw new Exception();
                               switch (reader.Value.ToLower())
                               {
     
                                   case "namedfield":
                                       NamedField el = new NamedField();
                                       while (reader.MoveToNextAttribute())
                                        switch (reader.Name.ToLower())
                                        {
                                            case "label":
                                                el.Label.Text = reader.Value;
                                                break;
                                            case "labelfontsize":
                                                el.Label.FontSize = Convert.ToInt32(reader.Value);
                                                break;
                                            case "fieldfontsize":
                                                el.FieldFontSize = Convert.ToInt32(reader.Value);
                                                break;
                                            case "labelposition":
                                                el.LabelPosition = reader.Value;
                                                break;
                                            case "labelwidth":
                                                el.Label.Width = Convert.ToInt32(reader.Value);
                                                break;
                                            case "labelheight":
                                                el.Label.Height = Convert.ToInt32(reader.Value);
                                                break;
                                            case "fieldwidth":
                                                el.FieldWidth = Convert.ToInt32(reader.Value);
                                                break;
                                            case "fieldheight":
                                                el.FieldHeight = Convert.ToInt32(reader.Value);
                                                break;
                                            case "align":
                                                el.Align = reader.Value;
                                                break;
                                            default:
                                                throw new Exception();
                                            }
                                       element = el;
                                       break;
      
                                   case "label":
                                        Label lab = new Label();
                                        while (reader.MoveToNextAttribute())
                                            switch (reader.Name.ToLower())
                                            {
                                                case "labelfontsize":
                                                    lab.FontSize = Convert.ToInt32(reader.Value);
                                                    break;
                                                case "align":
                                                    lab.Align = reader.Value;
                                                    break;
                                                case "width":
                                                    lab.Width = CalculateWidth(reader.Value);
                                                    break;
                                                case "height":
                                                    lab.Height = CalculateHeight(reader.Value);
                                                    break;
                                                default:
                                                    throw new Exception();

                                            }
                                        element = lab;
                                       break;
      
                                   case "field":
                                       Field fil = new Field();

                                       element = fil;
                                       break;
                                   case "spacing":
                                       //element = new Spacing();
                                       break;
                                   default: 
                                       {
                                           //var r = reader;
                                           throw new Exception();
                                           //break;
                                       }
                               }
                               break;

                       }                       
                       break;
                   case XmlNodeType.Text: 
                       TextValue = (reader.Value);
                       break;
                   case XmlNodeType.EndElement:
                       switch (reader.Name.ToLower())
                       {
                           case "section":
                               document.Sections.Enqueue(section);
                               break;
                           case "row":
                               section.Rows.Enqueue(row);
                               section.Rows.Enqueue(new RowSpace(8));
                               break;
                           case "column":
                               row.Columns.Enqueue(column);
                               break;
                           case "element":
                               element.Text = TextValue;
                               TextValue = "";
                               column.Elements.Enqueue(element);
                               break;
                           case "document":
                               break;

                       }
                       break;
               }
           }
           document.Save();
        }
    }
}
