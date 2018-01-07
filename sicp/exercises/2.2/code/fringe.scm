(define (fringe tree)
  ;;; Return a flattened version of the list `tree` (all the leaves arranged in
  ;;; left-to-right order)
  (define (flatten-tree res lst)
    (if (null? lst)
        res
        (let ((elem (car lst)))
          (if (list? elem)
              (flatten-tree (flatten-tree res elem)
                            (cdr lst))
              (flatten-tree (append res (list elem))
                            (cdr lst))))))
  (flatten-tree (list) tree))
