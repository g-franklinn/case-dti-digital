SELECT
    c.nome_cliente
    SUM(v.valor_venda) AS valor_total_gasto
FROM
    clientes c
JOIN
    vendas v ON c.id_cliente = v.id_cliente
GROUP BY
    c.nome_cliente
ORDER BY
    valor_total_gasto DESC