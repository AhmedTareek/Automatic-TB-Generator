`timescale 1ns / 1ps

module test_tb ();

    //Inputs
    reg A;
    reg B;
    reg  [1:0] C;
    reg  [1:0] D;

    //Outputs
    wire  [2:0] F;

    //Sequence
    reg [5:0] sequence = 0;

    //Instantiate the Design Under Test (DUT)
    test DUT (
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

      //Directed Stimulus Generation
      repeat(64)
      begin
          #10;
            A = sequence[0:0];
            B = sequence[1:1];
            C = sequence[3:2];
            D = sequence[5:4];
            sequence = sequence + 1;
      end

      #10;
      $finish;
  end
    
initial   //Analysis
   begin
        $display("Time"   , ,"A" , ,"B" , ,"C" , ,"D" , ,"F" );
        $monitor($time   , ,A , ,B , ,C , ,D , ,F );

  end
endmodule
