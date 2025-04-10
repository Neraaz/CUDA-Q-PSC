program openmp_example
  use omp_lib
  implicit none
  integer, parameter :: N = 1000000
  real :: array(N), sum
  integer :: i

  ! Initialize array
  array = 1.0

  sum = 0.0

  ! Parallel reduction sum
  !$omp parallel do reduction(+:sum)
  do i = 1, N
     sum = sum + array(i)
  end do
  !$omp end parallel do

  print *, 'Sum = ', sum

end program openmp_example

