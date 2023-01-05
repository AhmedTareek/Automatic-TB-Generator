`timescale 1ns / 1ps

module DecMuxAdd1_tb ();

    //Inputs

    //Outputs

    //Sequence
    reg [-1:0] sequence = 0;

    //Randomization
    integer seed = 5;

    //Instantiate the Design Under Test (DUT)
    DecMuxAdd1 DUT (
    );

  initial     //Stimulus
  begin
      //Initialize Inputs

      //Directed Stimulus Generation
      repeat(2)
      begin
          #10;
            sequence = sequence + 1;
      end

      #10;
      $finish;
  end
    
initial   //Analysis
   begin
        $display("             Time"   );
        $monitor($time   );

  end
endmodule
