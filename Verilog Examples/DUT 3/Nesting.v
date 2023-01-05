`timescale 1ns / 1ps

module Nesting(
    input [31:0] A,
    input [31:0] B,
    input [31:0] C,
    input [31:0] D,
    input en1,
    input en2,
    input [1:0] sel1,
    input [1:0] sel2,
    output reg [31:0] F
    );
	 
	 always @(A, B, C, D, en1, en2, sel1, sel2)
	 begin
			if(en1 == 1)
			begin
				case(sel1)
					2'b00: begin
								F[3:0] <= A[3:0];
								case(sel2)
									2'b00: F[7:4] <= A[7:4] & B[7:4];
									2'b01: F[7:4] <= A[7:4] | C[7:4];
									2'b10: F[7:4] <= A[7:4] ^ D[7:4];
									default: F[7:4] <= 0;
								endcase
							end
					2'b01: begin
								F[11:8] <= B[11:8];
								case(sel2)
									2'b00: F[15:12] <= A[15:12] & B[15:12];
									2'b01: F[15:12] <= A[15:12] | C[15:12];
									2'b11: F[15:12] <= ~A[15:12];
									default: F[15:12] <= 0;
								endcase
							end
					2'b10: begin
								F[19:16] <= C[19:16];
								case(sel2)
									2'b00: F[23:20] <= A[23:20] & B[23:20];
									2'b10: F[23:20] <= A[23:20] ^ D[23:20];
									2'b11: F[23:20] <= ~A[23:20];
									default: F[23:20] <= 0;
								endcase
							end
					default: begin
								F[27:24] <= D[27:24];
								case(sel2)
									2'b01: F[31:28] <= A[31:28] | C[31:28];
									2'b10: F[31:28] <= A[31:28] ^ D[31:28];
									2'b11: F[31:28] <= ~A[31:28];
									default: F[31:28] <= 0;
								endcase
							end
				endcase
			end
			else if(en2 == 1)
			begin
				F <= A|B|C|D;
			end
			else
			begin
				F <= 0;
			end
	 end


endmodule
