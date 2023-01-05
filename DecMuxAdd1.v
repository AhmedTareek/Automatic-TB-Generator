`timescale 1ns / 1ps

module DecMuxAdd1(
    input [1:0] sel1,
    input en,
    input [1:0] a,
    input [1:0] b,
    input [1:0] c,
    input [1:0] d,
    input [1:0] sel2,
    input X,
    input Y,
    input Ci,
    output [3:0] decout,
    output [1:0] muxout,
    output S,
    output Co
    );
	
	always @ (sel1, en)
	begin
		if (en == 0)
			decout = 4'b1111;
		else if (sel1 == 2'b00)
			decout = 4'b1110;
		else if (sel1 == 2'b01)
			decout = 4'b1101;
		else if (sel1 == 2'b10)
			decout = 4'b1011;
		else
			decout = 4'b0111;
	end
	
	always@ (a,b,c,d,sel2)
	begin
		case(sel2)
		 2'b00 : muxout=a;
		 2'b01 : muxout=b;
		 2'b10 : muxout=c;
		 2'b11 : muxout=d;
		 default : muxout=0;
		endcase
	end
	
	assign S  = X ^ Y ^ Ci;

	assign Co = (X & Y) | (X & Ci) | (Y & Ci);

endmodule
