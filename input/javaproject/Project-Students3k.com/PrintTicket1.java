import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PrintTicket1 extends JFrame
{
	public PrintTicket1(String sFrom, String sTo, String sClass, Integer iAdult, Integer iChildren, Integer iInfant, String sBookingDate, Integer iPrice, String sTime)
	{
		Container c=getContentPane();
		c.setLayout(new BorderLayout());


		JPanel Panel2 = new JPanel(null);

		Panel2.setPreferredSize(new Dimension(500,200));

		JLabel LTitle;
		JLabel LFrom ;
		JLabel LTo;
		JLabel LClass;
		JLabel LBookingDate;
		JLabel LPrice;
		JLabel LTime;
		JLabel LAdult;
		JLabel LChildren;
		JLabel LInfant;
		JLabel LWishes;


		JLabel LTicketNo;
		JLabel LBookedBy;

		JLabel LEmpty;
		JLabel LDemo;
		JLabel LFranklin;
		JLabel LRavi;
		JLabel LMayuran;
		JLabel LSathya;




		//pack();
		setSize(700,650);
		setVisible(true);
	}
}
