`timescale 1ns / 1ps

module modu_tb ();

    //Inputs
    reg A;
    reg B;
    reg  [1:0] C;
    reg  [1:0] D;

    //Outputs
    wire  [2:0] F;

    //Instantiate the Design Under Test (DUT)
    modu DUT (
        .A(A),
        .B(B),
        .C(C),
        .D(D),
        .F(F)
    );

  initial     //Stimulus
   begin
     //Initialize Inputs
        A = 0;
        B = 0;
        C = 0;
        D = 0;

      //Algorithmic Stimulus Generation

      #10;
        A = 1;
        B = 0;
        C = 0;
        D = 0;

      #10;
        A = 0;
        B = 1;
        C = 0;
        D = 0;

      #10;
        A = 1;
        B = 1;
        C = 0;
        D = 0;

      #10;
        A = 0;
        B = 0;
        C = 1;
        D = 0;

      #10;
        A = 1;
        B = 0;
        C = 1;
        D = 0;

      #10;
        A = 0;
        B = 1;
        C = 1;
        D = 0;

      #10;
        A = 1;
        B = 1;
        C = 1;
        D = 0;

      #10;
        A = 0;
        B = 0;
        C = 2;
        D = 0;

      #10;
        A = 1;
        B = 0;
        C = 2;
        D = 0;

      #10;
        A = 0;
        B = 1;
        C = 2;
        D = 0;

      #10;
        A = 1;
        B = 1;
        C = 2;
        D = 0;

      #10;
        A = 0;
        B = 0;
        C = 3;
        D = 0;

      #10;
        A = 1;
        B = 0;
        C = 3;
        D = 0;

      #10;
        A = 0;
        B = 1;
        C = 3;
        D = 0;

      #10;
        A = 1;
        B = 1;
        C = 3;
        D = 0;

      #10;
        A = 0;
        B = 0;
        C = 0;
        D = 1;

      #10;
        A = 1;
        B = 0;
        C = 0;
        D = 1;

      #10;
        A = 0;
        B = 1;
        C = 0;
        D = 1;

      #10;
        A = 1;
        B = 1;
        C = 0;
        D = 1;

      #10;
        A = 0;
        B = 0;
        C = 1;
        D = 1;

      #10;
        A = 1;
        B = 0;
        C = 1;
        D = 1;

      #10;
        A = 0;
        B = 1;
        C = 1;
        D = 1;

      #10;
        A = 1;
        B = 1;
        C = 1;
        D = 1;

      #10;
        A = 0;
        B = 0;
        C = 2;
        D = 1;

      #10;
        A = 1;
        B = 0;
        C = 2;
        D = 1;

      #10;
        A = 0;
        B = 1;
        C = 2;
        D = 1;

      #10;
        A = 1;
        B = 1;
        C = 2;
        D = 1;

      #10;
        A = 0;
        B = 0;
        C = 3;
        D = 1;

      #10;
        A = 1;
        B = 0;
        C = 3;
        D = 1;

      #10;
        A = 0;
        B = 1;
        C = 3;
        D = 1;

      #10;
        A = 1;
        B = 1;
        C = 3;
        D = 1;

      #10;
        A = 0;
        B = 0;
        C = 0;
        D = 2;

      #10;
        A = 1;
        B = 0;
        C = 0;
        D = 2;

      #10;
        A = 0;
        B = 1;
        C = 0;
        D = 2;

      #10;
        A = 1;
        B = 1;
        C = 0;
        D = 2;

      #10;
        A = 0;
        B = 0;
        C = 1;
        D = 2;

      #10;
        A = 1;
        B = 0;
        C = 1;
        D = 2;

      #10;
        A = 0;
        B = 1;
        C = 1;
        D = 2;

      #10;
        A = 1;
        B = 1;
        C = 1;
        D = 2;

      #10;
        A = 0;
        B = 0;
        C = 2;
        D = 2;

      #10;
        A = 1;
        B = 0;
        C = 2;
        D = 2;

      #10;
        A = 0;
        B = 1;
        C = 2;
        D = 2;

      #10;
        A = 1;
        B = 1;
        C = 2;
        D = 2;

      #10;
        A = 0;
        B = 0;
        C = 3;
        D = 2;

      #10;
        A = 1;
        B = 0;
        C = 3;
        D = 2;

      #10;
        A = 0;
        B = 1;
        C = 3;
        D = 2;

      #10;
        A = 1;
        B = 1;
        C = 3;
        D = 2;

      #10;
        A = 0;
        B = 0;
        C = 0;
        D = 3;

      #10;
        A = 1;
        B = 0;
        C = 0;
        D = 3;

      #10;
        A = 0;
        B = 1;
        C = 0;
        D = 3;

      #10;
        A = 1;
        B = 1;
        C = 0;
        D = 3;

      #10;
        A = 0;
        B = 0;
        C = 1;
        D = 3;

      #10;
        A = 1;
        B = 0;
        C = 1;
        D = 3;

      #10;
        A = 0;
        B = 1;
        C = 1;
        D = 3;

      #10;
        A = 1;
        B = 1;
        C = 1;
        D = 3;

      #10;
        A = 0;
        B = 0;
        C = 2;
        D = 3;

      #10;
        A = 1;
        B = 0;
        C = 2;
        D = 3;

      #10;
        A = 0;
        B = 1;
        C = 2;
        D = 3;

      #10;
        A = 1;
        B = 1;
        C = 2;
        D = 3;

      #10;
        A = 0;
        B = 0;
        C = 3;
        D = 3;

      #10;
        A = 1;
        B = 0;
        C = 3;
        D = 3;

      #10;
        A = 0;
        B = 1;
        C = 3;
        D = 3;

      #10;
        A = 1;
        B = 1;
        C = 3;
        D = 3;

      #10;
        A = 0;
        B = 0;
        C = 0;
        D = 0;

      #10;
        $finish;
  end
    
initial   //Analysis
   begin
        $display("Time"   , ,"A" , ,"B" , ,"C" , ,"D" , ,"F" );
        $monitor($time   , ,A , ,B , ,C , ,D , ,F );

  end
endmodule
