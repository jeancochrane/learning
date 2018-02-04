(define (accumulate op initial sequence)
  ;;; Apply the operator `op` to the list `sequence`, with the base case
  ;;; `initial`
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
