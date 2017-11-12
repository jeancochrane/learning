(define (pascal row col)
  ;;; Calculate a value in Pascal's triangle for a given row and col
  (cond ((or (= col 1) (= row col)) 1)
        ((or (< col 1) (> col row)) 0)
        (else (+ (pascal (- row 1) (- col 1))
                 (pascal (- row 1) col)))))

(define (coef n)
  ;;; Display the binomial coefficients for `n`
  (define (pascal-row row col)
    (if (= row col)
        (write-to-string (pascal row col))
        (string-append (write-to-string (pascal row col))
                        " "
                        (pascal-row row (+ col 1)))))
  (pascal-row n 1))

(define (pascals-triangle n)
  ;;; Display an inverted version of Pascal's triangle starting
  ;;; at row `n`
  (define (build-triangle n)
    (if (= n 1)
        (coef n)
        (string-append (coef n) "\n" (build-triangle (- n 1)))))
  (display (build-triangle n)))




