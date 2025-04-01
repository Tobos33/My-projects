package ZadB;
import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.JSlider.*;

import java.awt.*;
import java.awt.event.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;




public class MultiListenerFrame extends JFrame implements ActionListener {
	static final int MIN = 0;
	static final int MAX = 100;
	static final int INIT = 0;
	JSlider slider;
	JTextField field;
	
	public MultiListenerFrame() throws HeadlessException{
		this.setSize(640,480);
		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		this.setLayout(new BorderLayout());
		
		JPanel northPanel = new JPanel();
		northPanel.setBackground(Color.green);
		JPanel southPanel = new JPanel();
		southPanel.setBackground(Color.blue);
		JPanel eastPanel = new JPanel();
		eastPanel.setBackground(Color.black);
		JPanel westPanel = new JPanel();
		westPanel.setBackground(Color.red);
		westPanel.setLayout(new GridLayout(3, 1));
		JPanel centerPanel = new JPanel();
		
		
		JSlider slider = new JSlider(JSlider.HORIZONTAL, MIN, MAX, INIT);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(10);
		slider.setPaintTicks(true);
		slider.setPaintLabels(true);
		northPanel.add(slider);
		
		JButton button = new JButton("Zmien kolor");
		southPanel.add(button);
		
		JRadioButton top = new JRadioButton("top");
		westPanel.add(top);
		JRadioButton middle = new JRadioButton("middle");
		westPanel.add(middle);
		JRadioButton bottom = new JRadioButton("bottom");
		westPanel.add(bottom);
		
		ButtonGroup group = new ButtonGroup();
		group.add(top);
		group.add(middle);
		group.add(bottom);
		
		JTextField field = new JTextField(String.format("%d", slider.getValue()));
		eastPanel.add(field);
		slider.addChangeListener(new SliderChangeListener());
		
		
		this.add(northPanel, BorderLayout.NORTH);
		this.add(southPanel, BorderLayout.SOUTH);
		this.add(eastPanel, BorderLayout.EAST);
		this.add(westPanel, BorderLayout.WEST);
		this.add(centerPanel, BorderLayout.CENTER);
		
		
		
	}
	
	public class SliderChangeListener implements ChangeListener{
		
		@Override
		public void stateChanged(ChangeEvent arg0) {
			String value = String.format("%d", slider.getValue());
			field.setText(value);
		}
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub

	}
	public static void main(String[] args) {
		MultiListenerFrame frame = new MultiListenerFrame();
		frame.setVisible(true);
	}
	


}
