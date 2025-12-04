
module adder_16bit
(
    input logic [15:0] a, b,
    output logic [15:0] sum,
    output logic carry_out
);
    logic [3:0] pg_out, gg_out, input_carry;

    assign carry_out = input_carry[4];

    assign input_carry[0] = 0;
    assign input_carry[1] = gg_out[0] | (pg_out[0] & input_carry[0]);
    assign input_carry[2] = gg_out[1] | (pg_out[1] & input_carry[1]);
    assign input_carry[3] = gg_out[2] | (pg_out[2] & input_carry[2]);
    
    generate 
        for  (genvar i = 0; i < 4; i++) begin
            cla_block CB (.a(a[i*4-1:0]), .b(b[i*4-1:0]), .carry_in(input_carry[i]), .sum(sum[i*4-1:0]), .pg(pg_out[i]), .gg(gg_out[i]));
        end
    endgenerate


endmodule