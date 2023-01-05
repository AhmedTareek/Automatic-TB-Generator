`timescale 1ns / 1ps

module serializer_tb ();

    //Inputs
    reg clk;
    reg load;
    reg  [7:0] in_value;

    //Outputs
    wire o_bit;

    //Sequence
    reg [9:0] sequence = 0;

    //Randomization
    integer seed = 5;

    //Instantiate the Design Under Test (DUT)
    serializer DUT (
        .clk(clk),
        .load(load),
        .in_value(in_value),
        .o_bit(o_bit)
    );

  initial     //Stimulus
  begin
      //Initialize Inputs
        clk = 0;
        load = 0;
        in_value = 0;

      //Directed Stimulus Generation
      repeat(1025)
      begin
          #10;
            clk = sequence[0:0];
            load = sequence[1:1];
            in_value = sequence[9:2];
            sequence = sequence + 1;
      end

      #10;
      $finish;
  end
    
initial   //Analysis
   begin
        $display("             Time"   , ,"clk" , ,"load" , ,"in_value" , ,"o_bit" );
        $monitor($time   , ,clk , ,load , ,in_value , ,o_bit );

  end
endmodule
