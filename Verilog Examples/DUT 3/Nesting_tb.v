`timescale 1ns / 1ps

module Nesting_tb ();

    //Inputs
    reg  [31:0] A;
    reg  [31:0] B;
    reg  [31:0] C;
    reg  [31:0] D;
    reg en1;
    reg en2;
    reg  [1:0] sel1;
    reg  [1:0] sel2;

    //Outputs
    wire  [31:0] F;

    //Randomization
    integer seed = 5;

    //Instantiate the Design Under Test (DUT)
    Nesting DUT (
        .A(A),
        .B(B),
        .C(C),
        .D(D),
        .en1(en1),
        .en2(en2),
        .sel1(sel1),
        .sel2(sel2),
        .F(F)
    );

  initial     //Stimulus
  begin
      //Initialize Inputs
        A = 0;
        B = 0;
        C = 0;
        D = 0;
        en1 = 0;
        en2 = 0;
        sel1 = 0;
        sel2 = 0;

      //Randomized Stimulus Generation
    repeat(100000)
      begin
          #10;
            A = $random(seed);
            B = $random(seed);
            C = $random(seed);
            D = $random(seed);
            en1 = $random(seed);
            en2 = $random(seed);
            sel1 = $random(seed);
            sel2 = $random(seed);
        end

      //Testing design behaviour against don't care inputs
          #10;
            A = 1'bX;
            B = 1'bX;
            C = 1'bX;
            D = 1'bX;
            en1 = 1'bX;
            en2 = 1'bX;
            sel1 = 1'bX;
            sel2 = 1'bX;

      #10;
      $finish;
  end
    
initial   //Analysis
   begin
        $display("             Time"   , ,"A" , ,"B" , ,"C" , ,"D" , ,"en1" , ,"en2" , ,"sel1" , ,"sel2" , ,"F" );
        $monitor($time   , ,A , ,B , ,C , ,D , ,en1 , ,en2 , ,sel1 , ,sel2 , ,F );

  end
endmodule
