(define (element-of-set? x set)
  (cond ((null? set) false)
        ((= x (car set)) true)
        ((< x (car set)) false)
        (else (element-of-set? x (cdr set)))))

(define (intersection-set set1 set2)
  (if (or (null? set1) (null? set2))
      '()
      (let ((x1 (car set1)) (x2 (car set2)))
        (cond ((= x1 x2)
               (cons x1
                     (intersection-set (cdr set1)
                                       (cdr set2))))
              ((< x1 x2)
               (intersection-set (cdr set1) set2))
              ((< x2 x1)
               (intersection-set set1 (cdr set2)))))))

(define (adjoin-set x set)
  (define (adjoin x prev next)
    (cond ((null? next) (append prev (list x)))
          ((= x (car next)) set)
          ((< x (car next)) (append prev (append (list x) next)))
          (else (adjoin x (append prev (list (car next))) (cdr next)))))
  (adjoin x '() set))

;;; Tests
(adjoin-set 1 '(2 3 4))
;;; Expected: (1 2 3 4)

(adjoin-set 5 '(2 3 4))
;;; Expected: (2 3 4 5)

(adjoin-set 4 '(2 3 5))
;;; Expected: (2 3 4 5)
