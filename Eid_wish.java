import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Eid_wish extends JPanel implements ActionListener{
    private String message = "✨ Eid Mubarak! May your life be full of joy and blessings! 🌙";
    private int x = -800;
    private Timer timer;
    
    public Eid_wish(){
        setBackground(Color.BLACK);
        setForeground(Color.GREEN);
        setFont(new Font("Serif", Font.ITALIC,27));

        timer = new Timer(20,this);
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g){
        super.paintComponent(g);
        g.setColor(getForeground());
        g.setFont(getFont());
        g.drawString(message,x,getHeight()/2);
    }

    @Override
    public void actionPerformed(ActionEvent e){
        x+=4;
        if (x>getWidth())x = -message.length()*10;
        repaint();
    }

    public static void main(String[] args){
        JFrame frame = new JFrame("Eid Wish");
        frame.setSize(1280,720);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);

        Eid_wish animationPanel = new Eid_wish();
        frame.add(animationPanel);

        frame.setVisible(true);
    }
}