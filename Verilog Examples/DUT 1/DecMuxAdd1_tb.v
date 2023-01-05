`timescale 1ns / 1ps

module DecMuxAdd1_tb ();

    //Inputs
    reg  [1:0] sel1;
    reg en;
    reg  [1:0] a;
    reg  [1:0] b;
    reg  [1:0] c;
    reg  [1:0] d;
    reg  [1:0] sel2;
    reg X;
    reg Y;
    reg Ci;

    //Outputs
    wire  [3:0] decout;
    wire  [1:0] muxout;
    wire S;
    wire Co;

    //Sequence
    reg [15:0] sequence = 0;

    //Instantiate the Design Under Test (DUT)
    DecMuxAdd1 DUT (
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

      //Directed Stimulus Generation
      repeat(65537)
      begin
          #10;
            sel1 = sequence[1:0];
            en = sequence[2:2];
            a = sequence[4:3];
            b = sequence[6:5];
            c = sequence[8:7];
            d = sequence[10:9];
            sel2 = sequence[12:11];
            X = sequence[13:13];
            Y = sequence[14:14];
            Ci = sequence[15:15];
            sequence = sequence + 1;
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
