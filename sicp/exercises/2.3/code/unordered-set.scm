(define (element-of-set? x set)
  (cond ((null? set) false)
        ((equal? x (car set)) true)
        (else (element-of-set? x (cdr set)))))

(define (adjoin-set x set)
  (if (element-of-set? x set)
      set
      (cons x set)))

(define (intersection-set set1 set2)
  (cond ((or (null? set1) (null? set2)) '())
        ((element-of-set? (car set1) set2)
         (cons (car set1)
               (intersection-set (cdr set1) set2)))
        (else (intersection-set (cdr set1) set2))))

(define (union-set set1 set2)
  ;;; Find the overlap (union) between two sets
  (if (or (null? set1) (null? set2))
      set2
      (union-set (cdr set1) (adjoin-set (car set1) set2))))

;;; Tests
(union-set (list 1 3 4 2) (list 2 1 5))
;;; Expected: (4 3 2 1 5)

