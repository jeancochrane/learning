(define (element-of-set? x set)
  ;;; Same as the representation without duplicates
  (cond ((null? set) false)
        ((equal? x (car set)) true)
        (else (element-of-set? x (cdr set)))))

(define (adjoin-set x set)
  ;;; Faster than the representation without duplicates
  (cons x set))

(define (intersection-set set1 set2)
  ;;; Same worst-case performance as the representation without duplicates,
  ;;; but slower on average because the sets can be arbitrarily bigger
  (cond ((or (null? set1) (null? set2)) '())
        ((element-of-set? (car set1) set2)
         (cons (car set1)
               (intersection-set (cdr set1) set2)))
        (else (intersection-set (cdr set1) set2))))

(define (union-set set1 set2)
  ;;; Same procedure as the representation without duplicates, but faster
  ;;; because adjoin-set doesn't have to iterate the whole set
  (if (or (null? set1) (null? set2))
      set2
      (union-set (cdr set1) (adjoin-set (car set1) set2))))
