public class HeightMap
{
  /** A two-dimensional array of height values, initialized in the constructor (not shown)
    * Guaranteed not to be null
    */
  private double[][] heights;


  /** @param r a valid row index in heights
    * @param c a valid column index in heights
    * @return true if the height at row r, column c is not at the edge of the 
    * two-dimensional array heights, and is greater in value than all 8 surrounding
    * values; false otherwise.
    */
  public boolean isPeak(int r, int c)
  {  /* to be implemented in part (a) */  }
 

  /** @return an ArrayList of String objects which give information on each peak in 
    * the two-dimensional array heights.
    * Each string is in the format "Peak at (r, c): Height h", where r and c
    * are the row and column index, and h is the height of the peak.
    */
  public ArrayList peakInfo()
  {  /* to be implemented in part (b) */  }

  // There may be instance variables, constructors and methods that are not shown.
}