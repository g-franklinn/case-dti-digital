SELECT
    c.nome_cliente
FROM
    clientes c
JOIN
    clientes c ON c.id_cliente = v.id_cliente
JOIN
    produtos p ON v.id_produto = p.id_produto
GROUP BY
    c.id_cliente, c.nome_cliente
HAVING
    COUNT(DISTINCT p.categoria) = (SELECT COUNT(DISTINCT categoria) FROM produtos);