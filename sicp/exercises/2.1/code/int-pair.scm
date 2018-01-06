(define logn
  (lambda (base x)
    (/ (log x) (log base))))

(define (cons a b)
  ;;; Store the pair `(a, b)` as the integer that is the product `2^a * 3^b`.
  (* (expt 2 a) (expt 3 b)))

(define (car x)
  (if (= 0 (remainder x 3))
      (car (/ x 3)) ;; Get rid of the unneeded term
      (logn 2 x)))

(define (cdr x)
  (if (= 0 (remainder x 2))
      (cdr (/ x 2))
      (round (logn 3 x))))
