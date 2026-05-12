 public class games{   
    private int score=0;
    private int fire=0;
    private int live=0;
    private int lives=3;
    private int x=0;
    private int y=0;
    private int z=0;
    private int w=0;
    private int h=0;
    private boolean ends=false;
    private int camera=0;
    private int enemy=0;
    private int enemycount=3;
    
    private int tsleep=90000000;
    void usleep(int u){
        int i=9000000;
        int n=0;
        int m=0;
        for(m=0;m<u;m++){
            for(n=0;n<i;n++);
        }
    }
    void debugs(String c){
       System.out.println(c);
        usleep(tsleep);
    }
    void checkgameover(){
        //put you code here
        debugs("checkgameover\n\n");
    
    
    }
    void refreshscreen(){
        //put you code here
        debugs("refreshscreen");
    
    
    
    }
    void handlescore(){
        //put you code here
        debugs("handlescore");
    
    }
    void changenetwork(){
        //put you code here
        debugs("changenetwork");
    
    
    }
    void drawplayers(){
        //put you code here
        debugs("drawplayers");
    
    
    
    
    }
    void handlekeymouse(){
        //put you code here
        debugs("drawplayers");
    
    
    
    }
    void drawenemys(){
        //put you code here
        debugs("drawenemys");
    
    }
    void handlenemy(){
        //put you code here
        debugs("handlenemy");
    
    }
    void drawmain(){
        //put you code here
        debugs("drawmain");
    }
    
    void mainloop(){
        //put you code here
        debugs("mainloop");
        while(true){
            drawmain();
            handlenemy();
            drawenemys();
            handlekeymouse();
            drawplayers();
            changenetwork();
            handlescore();
            refreshscreen();
            checkgameover();
            if (ends)break;
        }
        
    }
    
    void setuploop(){
        //put you code here
        debugs("setuploop");
        while(true){
           mainloop();
           if (ends)break;
        }
        
        
    }
    public void main(String[] arg){
        //put you code here
        debugs("main");
        setuploop();
    
        
    }
}