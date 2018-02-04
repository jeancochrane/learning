(define (enumerate-integers start end)
  (define (enumerate x)
    (if (= x end)
        (list x)
        (append (list x) (enumerate (+ x 1)))))
  (cond ((< end start) (list))
        ((= end start) (list end))
        (else (enumerate start))))

(define (unique-pairs n)
  ;;; Generate the sequence of pairs (i, j) such that 1 < j < i < n
  (map (lambda (i)
         (map (lambda (j) (list i j))
                (enumerate-integers 1 (- i 1))))
       (enumerate-integers 1 n)))

;;; Tests
(enumerate-integers 1 5)
;;; Expected: (1 2 3 4 5)

(unique-pairs 3)
;;; Expected: ((2 1) (3 1) (3 2))
