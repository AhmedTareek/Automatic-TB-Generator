`timescale 1ns / 1ps

module DecMuxAdd2(
    input [3:0] sel1,
    input en,
    input [3:0] a,
    input [3:0] b,
    input [3:0] c,
    input [3:0] d,
    input [3:0] sel2,
    input [3:0] X,
    input [3:0] Y,
    input Ci,
    output reg [15:0] decout,
    output reg [3:0] muxout,
    output [3:0] S,
    output Co
    );
	 
	 reg [2:0] temp;
	
	always @ (sel1, en)
	begin
		if (en == 0)
			decout <= 16'bXXXXXXXXXXXXXXXX;
		else if (sel1 == 4'b0000)
			decout <= 16'b0000000000000001;
		else if (sel1 == 4'b0001)
			decout <= 16'b0000000000000010;
		else if (sel1 == 4'b0010)
			decout <= 16'b0000000000000100;
		else if (sel1 == 4'b0011)
			decout <= 16'b0000000000001000;
		else if (sel1 == 4'b0100)
			decout <= 16'b0000000000010000;
		else if (sel1 == 4'b0101)
			decout <= 16'b0000000000100000;
		else if (sel1 == 4'b0110)
			decout <= 16'b0000000001000000;
		else if (sel1 == 4'b0111)
			decout <= 16'b0000000010000000;
		else if (sel1 == 4'b1000)
			decout <= 16'b0000000100000000;
		else if (sel1 == 4'b1001)
			decout <= 16'b0000001000000000;
		else if (sel1 == 4'b1010)
			decout <= 16'b0000010000000000;
		else if (sel1 == 4'b1011)
			decout <= 16'b0000100000000000;
		else if (sel1 == 4'b1100)
			decout <= 16'b0001000000000000;
		else if (sel1 == 4'b1101)
			decout <= 16'b0010000000000000;
		else if (sel1 == 4'b1110)
			decout <= 16'b0100000000000000;
		else
			decout <= 16'b1000000000000000;
	end
	
	always@ (a,b,c,d,sel2)
	begin
		case(sel2)
		 4'b0000 : muxout <= a;
		 4'b0001 : muxout <= b;
		 4'b0010 : muxout <= c;
		 4'b0011 : muxout <= d;
		 4'b0100 : muxout <= a&b;
		 4'b0101 : muxout <= a|b;
		 4'b0110 : muxout <= a&c;
		 4'b0111 : muxout <= a|c;	
		 4'b1000 : muxout <= a&d;
		 4'b1001 : muxout <= a|d;
		 4'b1010 : muxout <= b&c;
		 4'b1011 : muxout <= b|c;
		 4'b1100 : muxout <= b&d;
		 4'b1101 : muxout <= b|d;
		 4'b1110 : muxout <= c&d;
		 4'b1111 : muxout <= c|d;			 
		 default : muxout <= 0;
		endcase
	end
	
	assign S[0]  = X[0] ^ Y[0] ^ Ci;
	assign temp[0] = (X[0] & Y[0]) | (X[0] & Ci) | (Y[0] & Ci);
	
	assign S[1] = X[1] ^ Y[1] ^ temp[0];
	assign temp[1] = (X[1] & Y[1]) | (X[1] & temp[0]) | (Y[1] & temp[0]);
	
	assign S[2] = X[2] ^ Y[2] ^ temp[1];
	assign temp[2] = (X[2] & Y[2]) | (X[2] & temp[1]) | (Y[2] & temp[1]);
	
	assign S[3] = X[3] ^ Y[3] ^ temp[2];
	assign Co = (X[3] & Y[3]) | (X[3] & temp[2]) | (Y[3] & temp[2]);

endmodule
