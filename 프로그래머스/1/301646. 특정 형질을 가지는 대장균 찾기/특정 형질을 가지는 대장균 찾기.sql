SELECT COUNT(id) AS COUNT
FROM ecoli_data
WHERE (genotype&2=0) AND (genotype&1=1 OR genotype&4=4)
