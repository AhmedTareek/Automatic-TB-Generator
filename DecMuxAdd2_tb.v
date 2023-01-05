`timescale 1ns / 1ps

module DecMuxAdd2_tb ();

    //Inputs
    reg  [3:0] sel1;
    reg en;
    reg  [3:0] a;
    reg  [3:0] b;
    reg  [3:0] c;
    reg  [3:0] d;
    reg  [3:0] sel2;
    reg  [3:0] X;
    reg  [3:0] Y;
    reg Ci;

    //Outputs
    wire  [15:0] decout;
    wire  [3:0] muxout;
    wire  [3:0] S;
    wire Co;

    //Randomization
    integer seed = 5;

    //Instantiate the Design Under Test (DUT)
    DecMuxAdd2 DUT (
        .sel1(sel1),
        .en(en),
        .a(a),
        .b(b),
        .c(c),
        .d(d),
        .sel2(sel2),
        .X(X),
        .Y(Y),
        .Ci(Ci),
        .decout(decout),
        .muxout(muxout),
        .S(S),
        .Co(Co)
    );

  initial     //Stimulus
  begin
      //Initialize Inputs
        sel1 = 0;
        en = 0;
        a = 0;
        b = 0;
        c = 0;
        d = 0;
        sel2 = 0;
        X = 0;
        Y = 0;
        Ci = 0;

      //Randomized Stimulus Generation
    repeat(100000)
      begin
          #10;
            sel1 = $random(seed);
            en = $random(seed);
            a = $random(seed);
            b = $random(seed);
            c = $random(seed);
            d = $random(seed);
            sel2 = $random(seed);
            X = $random(seed);
            Y = $random(seed);
            Ci = $random(seed);
        end

      //Testing design behaviour against don't care inputs
          #10;
            sel1 = 1'bX;
            en = 1'bX;
            a = 1'bX;
            b = 1'bX;
            c = 1'bX;
            d = 1'bX;
            sel2 = 1'bX;
            X = 1'bX;
            Y = 1'bX;
            Ci = 1'bX;

      #10;
      $finish;
  end
    
initial   //Analysis
   begin
        $display("             Time"   , ,"sel1" , ,"en" , ,"a" , ,"b" , ,"c" , ,"d" , ,"sel2" , ,"X" , ,"Y" , ,"Ci" , ,"decout" , ,"muxout" , ,"S" , ,"Co" );
        $monitor($time   , ,sel1 , ,en , ,a , ,b , ,c , ,d , ,sel2 , ,X , ,Y , ,Ci , ,decout , ,muxout , ,S , ,Co );

  end
endmodule
