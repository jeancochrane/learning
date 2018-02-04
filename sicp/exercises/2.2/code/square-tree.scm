(define (square-tree tree)
  ;;; Direct implementation of list squarer (without using map)
  (cond (null? tree) (list) ; Base case
        (not (pair? tree) (square tree))
        (else (cons (square-tree (car tree))
                    (square-tree (cdr tree))))))

(define (map-square-tree tree)
  ;;; Implementation of `square-tree` using `map` and recursion
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
            (map-square-tree sub-tree)
            (square sub-tree)))
       tree))
