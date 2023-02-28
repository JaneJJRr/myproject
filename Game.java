import java.util.List;
import java.util.ArrayList;
import javax.swing.*;
public class Game 
{
    public static void main(String args[]){
        Game Obj = new Game(); //เรียกฟังก์ชัน
        Obj.code();
        }   
    
    public void code(){
        Card objCard = new Card();
        objCard.shuffle(30);
        System.out.println("____________________________");
        System.out.println(" ♛  Welcome Game Bigjoke ♛ ");
        System.out.println("____________________________");
        for (int i = 0 ; i<1  ; i++){
            int cardValue = objCard.getCard(i);
            System.out.println("🐯 Tiger : " +  
            " : " + objCard.getCurrentRank() 
            + objCard.getCurrentSuit());
            int cardValue2 = objCard.getCard(i+2);
            System.out.println("🦐 Dragon : " +  
            " : " + objCard.getCurrentRank() 
            +objCard.getCurrentSuit());
            //สร้างตัวแปรขึ้นมาเก็บค่า
            int Score = cardValue;
            int Score2 = cardValue2;
            System.out.println("___________Score_________");
            //เปลี่ยนค่า
            cardValue = cardValue % 13;
            cardValue2 = cardValue2 % 13;
            Score = Score / 13; 
            Score2 = Score2 / 13; 
            if(cardValue > cardValue2){
                System.out.println(" 🐯 tiger to win ♛ ");
            
            }
                
            else if (cardValue < cardValue2){
                System.out.println(" 🦐 dragon to win ♛ ");
            
            }
            
            else {
                    if(Score < Score2){
                        System.out.println(" 🐯 tiger to win ♛ ");
            
                    }
                
                    else if (Score > Score2){
                        System.out.println(" 🦐 dragon to win ♛ ");
            
                    }
            }
        }    
        //เรียกฟังก์ชันมาใช้งาน
        int n = JOptionPane.showConfirmDialog(
                null,
                "Do you want to continue playing?",
                "An Inane Question",
                JOptionPane.YES_NO_OPTION);
        if(n==JOptionPane.YES_OPTION){
            code();
        }
        }
}

