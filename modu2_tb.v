`timescale 1ns / 1ps

module modu2_tb ();

    //Inputs
    reg A;
    reg B;
    reg  [9:0] C;
    reg  [9:0] D;

    //Outputs
    wire  [10:0] F;

    //Sequence
    reg [21:0] sequence = 0;

    //Randomization
    integer seed = 5;

    //Instantiate the Design Under Test (DUT)
    modu2 DUT (
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

      //Randomized Stimulus Generation
    repeat(100000)
      begin
          #10;
            A = $random(seed);
            B = $random(seed);
            C = $random(seed);
            D = $random(seed);
        end

      #10;
      $finish;
  end
    
initial   //Analysis
   begin
        $display("             Time"   , ,"A" , ,"B" , ,"C" , ,"D" , ,"F" );
        $monitor($time   , ,A , ,B , ,C , ,D , ,F );

  end
endmodule
