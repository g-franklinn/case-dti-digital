SELECT
    p.nome_produto
    COUNT(v.id_produto) AS quantidade_total_vendida
FROM
    produtos p
JOIN
    produtos p on v.id_produto = p.id_produto
WHERE
    v.data_venda >= DATE('now', '-1 month')
GROUP BY
    p.nome_produto
ORDER BY
    quantidade_total_vendida DESC
LIMIT 5;