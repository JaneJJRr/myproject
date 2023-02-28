
public class Card
{
    private int[] deck = new int[52];
    private String[] suits = { "♠","♥","♦","♣" };
    private String[] ranks = {"A","2","3","4","5","6","7","8","9","10","J","Q","K" };
    
    private String currentSuit;
    private String currentRank;
    private int currentIndex;
    
    public int getCurrentIndex(){
        return this.currentIndex;
    }
    
    public void nextCard(){
        this.currentIndex++;
    }
    
    public String getCurrentSuit(){
        return this.currentSuit;
    }
    
    public String getCurrentRank(){
        return this.currentRank;
    }
    
    public int[] getDeck(){
        return this.deck;
    }

    public int getCard(int index){
        currentSuit = suits[deck[index] / 13];
        currentRank = ranks[deck[index] % 13];
        
        return this.deck[index];
    }
    
    public Card(){
        for(int i=0;i < 52; i++){
            deck[i] = i;
        }
        this.currentIndex = 0;
    }
    
    public void shuffle(){
        for(int i=0; i<51; i++) {
            int index = (int)(Math.random() * 52);
            int temp = deck[i];
            if(index!=i){
                deck[i] = deck[index];
                deck[index] = temp;
            }
        }
        this.currentIndex = 0;
    }
    
    public void shuffle(int pCount){
        for(int i=0; i<pCount; i++) {
            int index = (int)(Math.random() * 52);
            
            int x = (int)(Math.random() * 52);
            int temp = deck[x];
            
            if(index!=x){
                deck[x] = deck[index];
                deck[index] = temp;
            }
            
        }
    }
}