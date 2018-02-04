(load "/home/jean/learning/sicp/exercises/2.2/code/accumulate-n.scm")

(define (dot-product v w)
  (accumulate + 0 (map * v w)))

(define (matrix-*-vector m v)
  (map (lambda (row) (dot-product row v)) m))

(define (transpose mat)
  (accumulate-n cons (list) mat))

(define (matrix-*-matrix m n)
  (let ((cols (transpose n)))
    (map (lambda (row) (matrix-*-vector cols row)) m)))

;; Tests
(let ((m (list (list 1 2 1) (list 0 1 0) (list 2 3 4)))
      (v (list 2 6 1)))
  (matrix-*-vector m v))
;; Expected: (15 6 26)

(let ((m (list (list 1 2 1) (list 0 1 0) (list 2 3 4))))
  (transpose m))
;; Expected: ((1 0 2) (2 1 3) (1 0 4))

(let ((m (list (list 1 2 1) (list 0 1 0) (list 2 3 4))))
  (matrix-*-matrix m m))
;; Expected: ((3 7 5) (0 1 0) (10 19 18))
